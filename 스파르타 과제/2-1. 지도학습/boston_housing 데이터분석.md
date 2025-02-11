
#  **보스턴 주택 가격 데이터 분석 보고서**

---

##  **1. 데이터 개요 및 전처리**

### **1.1 데이터 로드 및 기본 정보**
- **데이터셋**: 보스턴 주택 가격 데이터셋
- **목적**: 주택 가격(MEDV)에 영향을 미치는 주요 요인 분석 및 예측 모델 개발

** 확인된 내용:**
- 데이터에는 다수의 수치형 특성 존재
- 일부 결측치 및 이상치 발견

---

### **1.2 데이터 탐색 및 결측치 확인**
- **결측치**: 일부 열에 결측치 존재 → 적절한 처리 필요
- **기술 통계량**: 평균, 표준편차, 최소/최대값 분석
- **상관관계 분석**: 
   - RM(방 개수)와 MEDV 간의 강한 양의 상관관계
   - LSTAT(저소득층 비율)와 MEDV 간의 강한 음의 상관관계

---

### **1.3 이상치 탐지 및 제거**
이상치 제거를 위해 **세 가지 방법**이 사용됨:  
1. **현재 방식 (1%, 99%)**: 상하위 1%와 99% 이상치를 제거  
2. **IQR 방식**: 사분위수를 기준으로 이상치를 제거  
3. **Z-score 방식**: 평균과 표준편차를 기준으로 이상치를 제거  

---

##  **2. 이상치 제거 방법 비교**
### 1.1 **현재 방식 (1%, 99%)**  
- **설명**: 하위 1%와 상위 99%의 극단적 이상치를 제거  

**✅ 장점:**  
- 데이터 손실이 적음  
- 극단값만 제거하여 중요한 패턴을 보존  

**❌ 단점:**  
- 약한 이상치가 남을 수 있음  

---

### 1.2 **IQR (Interquartile Range) 방식**  
- **설명**: 사분위수를 기준으로 이상치를 판단하여 제거  

**✅ 장점:**  
- 통계적으로 검증된 방법  
- 분포에 따라 유연한 기준 적용  

**❌ 단점:**  
- 데이터 손실이 많을 수 있음  
- 정상 데이터가 제거될 가능성  

---

### 1.3 **Z-score 방식**  
- **설명**: 평균과 표준편차를 사용하여 이상치를 판단  

**✅ 장점:**  
- 정규분포를 가정할 때 효과적  
- 구현이 간단하고 직관적  

**❌ 단점:**  
- 비정규 분포에서는 부적절할 수 있음  
- 평균과 표준편차에 민감  

---

### **2.1 성능 비교 결과**

| **방법**           | **Samples** | **MAE** | **RMSE** | **R²** |
|--------------------|------------|---------|---------|-------|
| **Current (1%, 99%)** | 485        | 1.96    | 2.59    | 0.80  |
| **IQR**           | 412        | 2.15    | 2.85    | 0.75  |
| **Z-score**       | 458        | 2.08    | 2.75    | 0.77  |

** 분석 결과:**  
- **1%, 99% 방식**: 가장 높은 R² (0.80)과 낮은 RMSE (2.59) 기록  
- **Z-score 방식**: 두 번째로 우수한 성능  
- **IQR 방식**: 데이터 손실이 많아 성능 저하  

** 시각화 결과:**  
- RMSE, MAE, R² 모두 1%, 99% 방식이 우수한 성능을 보임  

---

##  **3. 모델 학습 및 성능 평가**

### **3.1 사용된 모델**
1. **Linear Regression**  
2. **Ridge Regression**  
3. **Decision Tree**  
4. **Random Forest**  
5. **Gradient Boosting**  
6. **SVR (Support Vector Regression)**  

### **3.2 하이퍼파라미터 최적화 (Random Forest)**  
- **최적 파라미터:**  
   - `n_estimators`: 200  
   - `max_depth`: 20  
   - `min_samples_split`: 5  
   - `min_samples_leaf`: 2  
   - `max_features`: 'sqrt'  

- **최적화된 RMSE:** 2.45  

---

### **3.3 모델별 성능 비교**

| **모델**             | **MAE** | **RMSE** | **R²** |
|----------------------|---------|---------|-------|
| **Linear Regression** | 2.35    | 3.12    | 0.72  |
| **Ridge**           | 2.30    | 3.05    | 0.73  |
| **Decision Tree**   | 2.10    | 2.85    | 0.75  |
| **Random Forest**   | 1.85    | 2.45    | 0.82  |
| **Gradient Boosting** | 1.95    | 2.55    | 0.80  |
| **SVR**            | 2.20    | 2.95    | 0.74  |

** 최종 분석 결과:**  
- **Random Forest**: 가장 높은 R² (0.82)와 가장 낮은 RMSE (2.45)  
- **Gradient Boosting**: 두 번째로 우수한 성능  
- **Linear Regression**: 가장 낮은 성능  

---

##  **4. 주요 특성 중요도 분석**

### **4.1 중요 특성 Top 5**
1. **LSTAT (저소득층 비율)**  
2. **RM (방 개수)**  
3. **NOX (일산화질소 농도)**  
4. **INDUS (비소매상업지역 비율)**  
5. **AGE (오래된 주택 비율)**  

**📊 시각화 결과:**  
- **LSTAT**과 **RM**이 주택 가격 예측에 가장 큰 영향을 미침  

---

##  **5. 교차 검증 결과**

- **Random Forest CV RMSE:** 2.50 (+/- 0.10)  
- **Gradient Boosting CV RMSE:** 2.60 (+/- 0.15)  

---

##  **6. 결론 및 인사이트**

1. **이상치 처리:**  
   - 1%, 99% 방식이 가장 적절한 방법으로 확인됨  

2. **모델 선택:**  
   - **Random Forest**가 주택 가격 예측에서 가장 우수한 성능을 보임  

3. **중요 특성:**  
   - **LSTAT**, **RM**, **NOX**가 주택 가격에 큰 영향을 미침  

4. **추천:**  
   - 이상치 제거는 1%, 99% 방식을 사용  
   - 주택 가격 예측은 **Random Forest** 모델을 사용  
