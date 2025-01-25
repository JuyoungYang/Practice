# Transformer 모델

Transformer 모델은 딥러닝에서 자연어 처리(NLP)와 컴퓨터 비전 등의 분야에서 혁신을 가져온 모델로, 
2017년 Google의 연구팀이 발표한 논문 "Attention is All You Need"에서 소개되었습니다. 
이 모델은 기존의 RNN(Recurrent Neural Networks)이나 LSTM(Long Short-Term Memory) 구조를 대체하며, Attention 메커니즘을 중심으로 작동합니다.

---

## 주요 특징

1. **Recurrent 구조 없이 병렬 처리 가능**
   - 시퀀스 데이터를 순차적으로 처리하지 않고 병렬로 처리합니다.
   - 훈련 속도가 빠르고 긴 시퀀스도 효과적으로 학습 가능합니다.

2. **Self-Attention 메커니즘**
   - 입력 시퀀스의 각 단어가 문장 내 다른 단어들과의 관계를 학습합니다.
   - 예: "The cat sat on the mat"에서 "cat"은 "sat"과 연관이 있음.

3. **입력 순서 정보 처리**
   - 시퀀스의 순서를 모델에 제공하기 위해 **Positional Encoding** 사용.

4. **Encoder-Decoder 구조**
   - Encoder는 입력 데이터를 처리하여 표현(embedding)을 생성.
   - Decoder는 이 표현을 기반으로 출력(예: 번역 결과)을 생성.

---

## 구조

Transformer는 **Multi-Head Attention**, **Feed-Forward Neural Network**, **Residual Connection**, **Layer Normalization**으로 구성됩니다.

### 1. Multi-Head Attention
- 입력 간의 관계를 병렬로 학습.
- Attention은 \( Q \) (Query), \( K \) (Key), \( V \) (Value) 행렬을 계산하여 단어 간의 중요도를 평가.

  Attention 계산 공식:
  \[
  \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
  \]

### 2. Feed-Forward Neural Network
- Attention의 출력을 비선형 변환.

### 3. Residual Connection과 Layer Normalization
- Gradient 소실 문제를 완화하고 안정적인 학습을 지원.

---

## 응용 분야

1. **언어 모델 (Language Modeling)**
   - BERT, GPT 등.
2. **번역 (Translation)**
   - 영어 ↔ 한국어 번역.
3. **컴퓨터 비전**
   - Vision Transformer(ViT)로 이미지 분류.
4. **멀티모달 학습**
   - 텍스트, 이미지, 음성 데이터를 함께 처리.

---

## 장점

- 병렬 처리로 훈련 속도가 빠름.
- 긴 시퀀스에서도 관계를 효과적으로 학습.
- 텍스트, 이미지, 영상 등 다양한 데이터에 적용 가능.


