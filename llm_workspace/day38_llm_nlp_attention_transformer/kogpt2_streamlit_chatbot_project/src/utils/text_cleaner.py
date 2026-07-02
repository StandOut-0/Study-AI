"""
KoGPT2 생성 결과를 화면에 보기 좋게 정리하는 유틸리티 파일입니다.

언어 모델은 토큰 단위로 문장을 생성하므로 특수 토큰, 제어 문자, 반복 공백 등이
섞일 수 있습니다. Streamlit 화면에 표시하기 전에 정리하면 결과가 더 읽기 좋아집니다.
"""

# 정규표현식 처리를 위한 파이썬 기본 라이브러리입니다.
# 제어 문자 제거, 반복 공백 축소 같은 문자열 정리에 사용합니다.
import re


# 생성된 문자열을 정리하는 함수를 정의합니다.
# text 매개변수에는 tokenizer.decode()로 복원된 문자열이 들어옵니다.
def clean_generated_text(text: str) -> str:
    # 유니코드 replacement character(�)는 디코딩 오류가 있을 때 나타날 수 있으므로 제거합니다.
    text = text.replace("�", "")

    # ASCII 제어 문자를 공백으로 바꿉니다.
    # 줄바꿈, 탭, 보이지 않는 문자가 섞이면 채팅 출력이 지저분해질 수 있습니다.
    text = re.sub(r"[\x00-\x1F\x7F]", " ", text)

    # KoGPT2에서 출력될 수 있는 문장 시작/종료 특수 토큰을 제거합니다.
    # 사용자가 읽는 답변에는 특수 토큰이 보이지 않는 것이 좋습니다.
    text = text.replace("</s>", " ")

    # 패딩 토큰 문자열을 제거합니다.
    # 패딩 토큰은 문장 길이를 맞추기 위한 기호이므로 최종 답변에는 필요하지 않습니다.
    text = text.replace("<pad>", " ")

    # 알 수 없는 토큰 문자열을 제거합니다.
    # 알 수 없는 토큰이 화면에 그대로 보이면 문장이 어색해 보일 수 있습니다.
    text = text.replace("<unk>", " ")

    # 마스크 토큰 문자열을 제거합니다.
    # GPT 생성에서는 주로 사용하지 않지만 출력될 경우를 대비합니다.
    text = text.replace("<mask>", " ")

    # 여러 개의 공백을 하나의 공백으로 줄입니다.
    # 토큰 디코딩 후 공백이 반복될 수 있으므로 보기 좋게 정리합니다.
    text = re.sub(r"\s+", " ", text)

    # 문장 앞뒤의 불필요한 공백을 제거합니다.
    # 최종 화면 출력이 깔끔해집니다.
    text = text.strip()

    # 정리된 문자열을 반환합니다.
    return text


# 챗봇 프롬프트를 구성하는 함수를 정의합니다.
# KoGPT2는 대화 전용으로 미세조정된 모델이 아니므로 역할 표시를 넣어 답변 방향을 잡습니다.
def build_chat_prompt(user_message: str, history: list[dict[str, str]] | None = None) -> str:
    # 대화 이력이 None이면 빈 리스트로 바꿉니다.
    # 이렇게 하면 이후 반복문에서 NoneType 오류가 발생하지 않습니다.
    history = history or []

    # 프롬프트에 들어갈 문자열 조각을 저장할 리스트를 만듭니다.
    # 여러 줄을 리스트에 담은 뒤 join하면 구조적인 프롬프트를 만들기 쉽습니다.
    prompt_parts: list[str] = []

    # 챗봇의 역할을 간단히 설명하는 시스템성 안내 문장을 추가합니다.
    # KoGPT2가 사용자의 질문에 이어 답변하도록 문맥을 제공합니다.
    prompt_parts.append("다음은 사용자와 한국어 인공지능 챗봇의 대화입니다.")

    # 최근 대화 이력만 프롬프트에 넣기 위해 마지막 3개 메시지를 사용합니다.
    # 너무 긴 이력을 넣으면 입력 토큰이 길어져 속도가 느려지고 답변 품질이 흔들릴 수 있습니다.
    recent_history = history[-3:]

    # 최근 대화 이력을 순서대로 프롬프트에 추가합니다.
    # role 값이 user이면 사용자 발화, assistant이면 챗봇 응답으로 표시합니다.
    for message in recent_history:
        # 현재 메시지의 역할 값을 가져옵니다.
        # 값이 없으면 빈 문자열을 사용하여 KeyError를 방지합니다.
        role = message.get("role", "")

        # 현재 메시지의 내용을 가져옵니다.
        # 값이 없으면 빈 문자열을 사용하여 KeyError를 방지합니다.
        content = message.get("content", "")

        # 사용자 메시지이면 "사용자:" 형식으로 추가합니다.
        # 이 형식은 모델이 대화 흐름을 구분하는 데 도움을 줍니다.
        if role == "user":
            prompt_parts.append(f"사용자: {content}")

        # 챗봇 메시지이면 "챗봇:" 형식으로 추가합니다.
        # 이전 답변을 함께 넣으면 짧은 문맥 유지에 도움이 됩니다.
        elif role == "assistant":
            prompt_parts.append(f"챗봇: {content}")

    # 현재 사용자의 새 입력을 프롬프트에 추가합니다.
    # 모델은 이 문장 뒤의 챗봇 답변을 생성하게 됩니다.
    prompt_parts.append(f"사용자: {user_message}")

    # 모델이 이어서 생성할 위치를 "챗봇:"으로 시작시킵니다.
    # 이렇게 하면 답변 형식이 비교적 일정하게 유지됩니다.
    prompt_parts.append("챗봇:")

    # 줄바꿈으로 프롬프트 조각을 연결합니다.
    # 대화 구조가 잘 보이도록 각 발화를 한 줄로 분리합니다.
    prompt = "\n".join(prompt_parts)

    # 완성된 프롬프트를 반환합니다.
    return prompt


# 모델 출력에서 챗봇 답변 부분만 잘라내는 함수를 정의합니다.
# 전체 디코딩 결과에는 입력 프롬프트까지 포함될 수 있으므로 후처리가 필요합니다.
def extract_answer(full_text: str, prompt: str) -> str:
    # 전체 생성 결과가 입력 프롬프트로 시작하면 프롬프트 부분을 제거합니다.
    # 이렇게 해야 사용자가 입력한 문장이 답변에 반복 표시되지 않습니다.
    if full_text.startswith(prompt):
        full_text = full_text[len(prompt):]

    # 혹시 남아 있는 "사용자:" 이후 문장은 다음 턴처럼 보일 수 있으므로 제거합니다.
    # 생성 모델이 대화 형식을 흉내 내며 새 사용자 발화를 만들어 내는 것을 막기 위한 후처리입니다.
    full_text = full_text.split("사용자:")[0]

    # 혹시 남아 있는 "챗봇:" 라벨을 제거합니다.
    # 화면에는 실제 답변 문장만 표시하는 것이 자연스럽습니다.
    full_text = full_text.replace("챗봇:", " ")

    # 공통 정리 함수를 적용하여 특수 토큰과 불필요한 공백을 제거합니다.
    answer = clean_generated_text(full_text)

    # 답변이 비어 있으면 기본 안내 답변을 사용합니다.
    # 모델이 종료 토큰만 생성하거나 너무 짧게 끝나는 경우를 대비합니다.
    if not answer:
        answer = "답변을 생성하지 못했습니다. 질문을 조금 더 구체적으로 입력해 주세요."

    # 최종 답변을 반환합니다.
    return answer
