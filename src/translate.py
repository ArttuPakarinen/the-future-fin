import logging
import os
import deepl
import requests
import sys

LOGGER = logging.getLogger(__name__)
ALLOWED_FILE_TYPES = {'txt', 'pdf'}


def get_char_size(content: str) -> int:
    return len(content.encode('utf-8'))


def open_file(relative_path: str, mode: str = 'r') -> str:
    module_path = os.path.abspath(__file__)
    path = os.path.join(os.path.dirname(module_path), relative_path)
    with open(path, mode) as f:
        return f.read()


def write_file(relative_path: str, content: str, target_lang: str, mode: str = 'w') -> str:
    module_path = os.path.abspath(__file__)
    path = os.path.join(os.path.dirname(module_path), relative_path)
    with open(path, mode) as f:
        return f.write(content)


def _validate_file(file_suffix: str, content: str) -> None:
    if file_suffix not in ALLOWED_FILE_TYPES:
        raise ValueError('File type not allowed. Only {} are allowed.'.format(ALLOWED_FILE_TYPES))
    if not content:
        raise ValueError('File is empty.')
    if get_char_size(content) > 5000000:
        raise ValueError('File is too large. Max size is 5MB.')
    return True


def _split_content(content: str, chars_per_chunk: int = 5000) -> list[str]:
    """Splits text (linewise) into smaller chunks based on chars_per_chunk."""
    chunks = []
    chunk = ''
    for line in content.splitlines():
        if get_char_size(chunk) + get_char_size(line) > chars_per_chunk:
            chunks.append(chunk)
            chunk = ''
        chunk += line + '\n'
    if chunk:
        chunks.append(chunk[:-1]) # The last separator must be omitted.
    return chunks


def translate_with_google(content: str, target_lang: str = 'en') -> str:
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={}&dt=t&q={}'
    url = url.format(target_lang, content)
    response = requests.get(url)
    if response.status_code != 200:
        print('Error: the translate API returned an unsuccessful status code {}'.format(response.status_code))
        sys.exit()
    return ''.join(t[0] for t in response.json()[0])


def _get_deepl_token() -> str:
    return os.getenv("DEEPL_TOKEN")


def _translate_with_deepl(content: str, target_lang: str = 'EN') -> str:
    """Translate the given text into the target language with deepl api.
    Use the access token to authenticate your request."""
    translator = deepl.Translator(_get_deepl_token())
    result = translator.translate_text(content, target_lang=target_lang)
    raw_text = result.text
    text = raw_text.replace('SIVUNVAIHTO', 'PAGE BREAK')
    return text


def translate_file(file_path, target_lang='EN') -> None: 
    content = open_file(file_path)
    file_suffix = file_path.split('.')[-1]
    _validate_file(file_suffix, content)
    res = _translate_with_deepl(content, target_lang=target_lang)
    saved_file_path = file_path.split('.' + file_suffix)[0] + '_' + target_lang.lower() + '.' + file_suffix
    write_file(saved_file_path, res, target_lang=target_lang)


if __name__ == '__main__':
    first_part = '../data/the_future_chapters_1-20.txt'
    second_part = '../data/the_future_chapters_21-37.txt'
    third_part = '../data/the_future_chapters_38-46.txt'
    content = open_file(first_part)
    print(get_char_size(content))
    content = open_file(second_part)
    print(get_char_size(content))
    content = open_file(third_part)
    print(get_char_size(content))

    #translate_file(first_part, 'FI')
