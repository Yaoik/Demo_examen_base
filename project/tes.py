import requests

cookies = {
    'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6ImpoR0VlRVJhZFRRSzlBdXBVZjY1SXc9PSIsInZhbHVlIjoiSy9aSlJQRVhSeHpEcHBZZHpFNE56TmVSRUVkaTJRTE5vT1pzODZteklkU0ZwOTJOZldCWEtBRUlVSDQvbnhISWFPZU9LemNtN3FnVHhqclNnMEJoNlZzNFQ4N3lpa3JsaFRtQlNLMDdxbU5YMkV0ZHE3TUFsMEtFYVNIbWpINHQyOWxYaDlTWENMQ1lRKzZxdmpxak9WdGY0ZGlkQ3VzYUcxcmFxUGloL29CSVk2NG16SmIvV1pEUFp2MGc5Q09oTnlybjh5Tk9YQWFWNm5KRTM4YXNpZz09IiwibWFjIjoiMTg0YWMwNzcwYjUxNjFkNjhmYmM4MTdmM2I5MmI1OTA5OTYwMDM3YWUxNWE4NGZmNWJiMjM2MGRmNjU3NjNmZSIsInRhZyI6IiJ9',
    'XSRF-TOKEN': 'eyJpdiI6ImMwUjR6UXMralN5YXhpSTdRY3Q2Qmc9PSIsInZhbHVlIjoiM2xlTGcxaStocWllbHFoNVlvUmN6TEw4dlJJb0FoVmxJYTFhV3I0M29WWXZRYlJWT2xTSDBDVzNIaVVHOFQwcXBURlE5VDZRUm0yWnppZW1pc0RtUTVRU3F3MFJRT3BxTnVYVTVsZWh4Q0FVOGNIYzA1YTJvczgxbGl3MDhYUCsiLCJtYWMiOiJiMmEzY2NhNzVhYjM0NzRlNmU5ZmY5NTRjZjg0MDc5MjhlOTdiMmM3NTMyZDVhMWEzMjg5ZmNkNzhiNDE2NzQzIiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6Im12cHMza3V3c0hHR09VTEV2RXhXL1E9PSIsInZhbHVlIjoiMzhkWmRXZlFmZFhxWmRMcWFQVE1SVGZyeW51S2YyRHl1amU2L0NraC9QSTVpUXRNSVRXdmcyRVI2ZGU3d0VZN3IvSThaVGNUWkh5b1VjcmFTMWFFVDMyUGF3MUQyNlFHNWZUS25PeURFWkZiKzJqYmtUalZtRHhKTjU5dUxMYWgiLCJtYWMiOiI3Njk4ZmVmNzE0ODFjYWQ1MWRiMjA5NDU2M2Q1Nzc5NTE0M2Y3MjZkZjY5NDdjMWVlMGVlZGU0NjE3ZTRiN2IwIiwidGFnIjoiIn0%3D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'http://26.132.214.251:8000',
    'Referer': 'http://26.132.214.251:8000/chat/20',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-KL-Ajax-Request': 'Ajax_Request',
    'content-type': 'application/json',
}

data = '{"chat_id":"20","text":"\u0425\u0430\u0439<div><br></div>"}'

response = requests.post('http://26.132.214.251:8000/api/chat/messages/add', headers=headers, cookies=cookies, data=data, verify=False)
