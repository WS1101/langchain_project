# 📈 Economic Insight Agent

**Economic Insight Agent**는 거시경제 흐름과 실시간 시장 데이터를 기반으로  
투자 판단을 보조하는 AI 경제 분석 에이전트입니다.

정적 경제 지식베이스와 실시간 뉴스 데이터를 결합하여  
사용자의 투자 성향에 맞춘 **맞춤형 경제 해석 및 투자 인사이트**를 제공합니다.

---

## 1. 프로젝트 개요 (Project Overview)

### 목적
거시경제 데이터와 최신 시장 정보를 종합 분석하여  
투자자가 경제 흐름을 이해하고 더 나은 판단을 내릴 수 있도록 지원

### 핵심 가치
- 거시경제 기반 투자 분석
- 실시간 뉴스 반영
- 사용자 맞춤형 해석
- RAG 기반 신뢰성 강화
- 경제 지표와 투자 전략 연결

---

## 2. 주요 기능 (Features)

### 맞춤형 투자 분석
사용자의 투자 성향과 보유 자산군을 반영

예시:
```plaintext
투자 성향: 보수형
보유 자산: 미국채 ETF, 배당주
````

---

### 거시경제 질의응답

경제 흐름에 대한 자연어 질문 가능

예시:

```plaintext
금리 인상이 장기채에 어떤 영향을 줄까?
```

---

### 실시간 뉴스 기반 분석

최신 시장 데이터 검색 후 답변 생성

반영 예시:

* 기준금리
* 유가
* 환율
* CPI
* 고용지표

---

### 내부 경제 전략 RAG 검색

사전에 구축한 경제 데이터셋에서 관련 전략 검색

검색 대상:

* 금리 사이클
* 경기 침체 패턴
* 채권 가격 메커니즘
* 자산군별 대응 전략

---

### 투자 책임 고지

직접적인 매수/매도 판단은 사용자에게 있음을 명확히 안내

---

## 3. 기술 스택 (Tech Stack)

### LLM

* **Groq**

  * 초고속 추론

* **Llama 3.1 8B Instant**

  * 경제 분석 응답 생성

---

### Embedding

* **Ollama**
* **nomic-embed-text-v2-moe**

경제 문서 벡터화

---

### Vector Database

* **FAISS**

고속 유사도 검색

---

### Framework

* **LangChain**

  * 체인 구성
  * Retriever 관리
  * Prompt orchestration

---

### External Search

* **Tavily Search API**

실시간 시장 뉴스 검색

---

### Environment

* **Python**
* **dotenv**

---

## 4. 시스템 아키텍처 (Architecture)

```plaintext id="k2px7n"
사용자 입력
   │
   ├── 투자 성향
   ├── 보유 자산군
   └── 경제 질문
        │
        ▼
입력 라우팅
        │
        ├── Vector Search (FAISS)
        └── 실시간 뉴스 검색 (Tavily)
                │
                ▼
컨텍스트 병합
        │
        ▼
LLM 분석
(Llama 3.1)
        │
        ▼
맞춤형 경제 분석 리포트
```

---

## 5. 프로젝트 구조 (Project Structure)

```plaintext id="p9a4lt"
Economic-Insight-Agent/
│
├── main.py
│   └── CLI 실행 파일
│
├── chain.py
│   └── LangChain 분석 체인
│
├── vectorstore.py
│   └── 벡터 저장/로드 관리
│
├── embeddings.py
│   └── 임베딩 모델 설정
│
├── dataset/
│   └── data.json
│
├── exp-faiss/
│   └── 저장된 벡터 DB
│
├── .env
│
└── README.md
```

---

## 6. 핵심 구성 요소 (Core Components)

## Vector Store

경제 전략 데이터셋을 임베딩 후 FAISS에 저장

### 역할

* 경제 지식 검색
* 과거 전략 참조
* 관련 경제 패턴 제공

---

## Retriever

질문과 가장 유사한 경제 문서 검색

```python id="7k0wre"
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)
```

---

## Tavily Search

실시간 경제 뉴스 검색

```python id="6u2x9m"
search = TavilySearchAPIRetriever(k=3)
```

---

## Prompt Engineering

응답 제약:

* 개발 내부 구조 비공개
* 실시간 수치 포함
* 구체적 데이터 기반 설명
* 투자 책임 명시

---

## 7. 설치 및 실행 (Getting Started)

### Prerequisites

* Python 3.10+
* Ollama 설치
* Groq API Key
* Tavily API Key

---

### 1. 저장소 클론

```bash id="n1k8xo"
git clone https://github.com/your-repo/Economic-Insight-Agent.git
cd Economic-Insight-Agent
```

---

### 2. 패키지 설치

```bash id="o7v2qi"
pip install -r requirements.txt
```

---

### 3. Ollama 모델 설치

```bash id="x8m5fj"
ollama pull nomic-embed-text-v2-moe
```

---

### 4. 환경 변수 설정

`.env`

```env id="4qjz7c"
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

---

### 5. 실행

```bash id="5l7qzr"
python main.py
```

---

## 8. 사용 방법 (Usage)

실행 후:

```plaintext id="n0j8ua"
질문이 필요하면 '1', 종료하려면 '0'
```

---

### 사용자 프로필 입력

```plaintext id="4ksqpf"
투자 성향: 공격형
보유 자산군: 미국 기술주, 비트코인
```

---

### 질문 입력

```plaintext id="hn7z9e"
최근 금리 동결이 성장주에 어떤 영향을 줄까?
```

---

### 출력 예시

```plaintext id="f5tx1n"
미 연준 기준금리가 5.25% 수준을 유지하면서
성장주 할인율 부담은 완화되었습니다.

다만 유가가 최근 4.8% 상승하며
인플레이션 재가속 우려가 존재합니다.

공격형 포트폴리오에서는
AI 반도체 및 대형 기술주 비중 확대가
유효할 수 있습니다.
```

---

## 9. 동작 방식 (Workflow)

### Step 1

사용자 질문 수신

---

### Step 2

FAISS에서 관련 거시경제 전략 검색

---

### Step 3

Tavily로 최신 뉴스 검색

---

### Step 4

LLM이 두 정보를 종합 분석

---

### Step 5

사용자 투자 성향 반영

---

### Step 6

최종 경제 인사이트 제공

---

## 10. 기대 효과 (Expected Outcomes)

### 정보 비대칭 완화

전문 경제 데이터를 쉽게 해석

---

### 투자 의사결정 보조

거시경제 기반 전략 수립 지원

---

### 학습형 투자 가능

단순 추천이 아닌 이유 중심 설명

---

## 11. 향후 개선 방향 (Future Work)

### Web Dashboard

CLI → Streamlit 웹 서비스 전환

---

### 포트폴리오 시뮬레이터

자산군별 시나리오 테스트

---

### 경제 이벤트 캘린더

FOMC / CPI 일정 자동 반영

---

### 시계열 분석

시장 추세 예측 기능 추가

---

### 멀티 에이전트 구조

* Macro Agent
* Bond Agent
* Equity Agent
* Risk Agent

---

## 12. 개발자 정보 (Developer)

**서우진 (Woojin Seo)**

거시경제 기반 AI 투자 보조 시스템 설계 및 개발

---


