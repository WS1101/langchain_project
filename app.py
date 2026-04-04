import os
from vectorstore import init_vectorstore, load_vector_from_local
from chain import build_economic_agent
from dotenv import load_dotenv



def main():
    load_dotenv()
    
    print("="*30)
    print("거시경제의 흐름을 바탕으로 정보를 제공하고 투자 선택에 도움을 주는 경제 AI 에이전트입니다.")
    print("="*30)

    # 1. 벡터 스토어 초기화 (기존 데이터가 없으면 생성, 있으면 로드)
    if not os.path.exists('./exp-faiss'):
        vectorstore = init_vectorstore()
    else:
        vectorstore = load_vector_from_local()

    # 2. 에이전트 체인 빌드 (3단계 고도화 로직 포함)
    agent_chain = build_economic_agent(vectorstore)

    while True:
        print()
        choice = input("질문이 필요하면 '1', 종료하려면 '0'을 누르세요: ")

        if choice == '0':
            print("경제 에이전트를 종료합니다. 성공적인 투자 되세요!")
            break
        
        elif choice == '1':
            print("\n--- [투자자 맞춤형 분석을 위한 기초 정보 입력] ---")
            profile = input("투자 성향(공격형/보수형)과 주요 보유 자산군을 입력하세요: ")
            question = input("경제 상황이나 채권 계산 등에 대해 질문하세요: ")
            
            print("\n에이전트가 분석 중입니다. 잠시만 기다려 주세요...")
            
            # 3. 에이전트 실행 (요구사항 1~5 통합 처리)
            # 인풋에 성향(profile)과 질문(question)을 함께 전달합니다.
            response = agent_chain.invoke({
                "profile": profile,
                "question": question
            })
            
            print("\n[AI 에이전트 분석 결과]")
            print("-" * 50)
            print(response)
            print("-" * 50)
            
        else:
            print("잘못된 입력입니다. '1' 또는 '0'을 입력해주세요.")

if __name__ == "__main__":
    main()