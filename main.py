
def add_new_sector(sector_list):
    """사용자로부터 새로운 재난 구역 정보를 입력받아 리스트에 추가하는 함수"""
    print("\n[➕ 새로운 재난 구역 추가]")
    
    # 1. 새로운 구역 ID 계산 (기존 리스트의 마지막 ID + 1)
    # 예: 마지막 구역 ID가 6이면 다음은 7
    next_id = sector_list[-1][0] + 1 if len(sector_list) > 0 else 1
    
    # 2. 사용자에게 구역 정보 입력받기
    name = input("▶️ 구역 이름을 입력하세요 (예: G-2 대피소): ")
    
    try:
        risk = int(input("▶️ 위험도 점수를 입력하세요 (0~100): "))
        time = int(input("▶️ 진입 소요 시간(분)을 입력하세요: "))
    except ValueError:
        print("❌ 위험도와 소요 시간은 숫자로 입력해야 합니다. 추가를 취소합니다.")
        return
        
    condition = input("▶️ 구역 특성을 입력하세요 (통신가능 / 붕괴위험 / 가스누출): ")
    
    # 3. 입력받은 데이터를 하나의 행(리스트)으로 묶기
    new_sector = [next_id, name, risk, time, condition]
    
    # 4. 2차원 리스트에 추가하기
    sector_list.append(new_sector) [cite: 8]
    print(f"✅ '{name}' 구역이 성공적으로 데이터베이스에 등록되었습니다!")

def show_robot_status():
    """로봇의 현재 시스템 상태를 안내하는 함수"""
    print("=" * 45)
    print("🤖 재난 구조 로봇 경로 탐색 시스템 활성화")
    print("=" * 45)

def search_safe_sectors(sector_list, max_risk, condition):
    """
    위험도 점수 이하이고 특성 조건이 맞는 구역을 필터링하는 함수
    (조건 필터링형 및 복합 조건 처리 알고리즘 구현)
    """
    filtered_list = []
    
    # 반복문을 통해 2차원 리스트의 각 행(구역)을 검사합니다.
    for sector in sector_list:
        if sector[2] <= max_risk and sector[4] == condition:
            filtered_list.append(sector)
    return filtered_list

def find_best_sector(filtered_list):
    """
    필터링된 구역 중 이동 소요 시간(인덱스 3)이 가장 짧은 최적 구역을 찾는 함수
    (분석 및 최솟값 탐색 알고리즘 구현)
    """
    # 예외 처리: 조건에 맞는 구역이 없으면 빈 값(None) 반환 [cite: 16, 25]
    if len(filtered_list) == 0:
        return None
    # 최솟값을 찾기 위해 첫 번째 항목을 기준으로 설정합니다.
    best = filtered_list[0]
    
    for sector in filtered_list:
        if sector[3] < best[3]:
            best = sector
    return best

def print_report(results, best_sector):
    """최종 탐색 결과를 출력하는 함수 (실행 결과 출력 필수 조건)"""
    print("\n[📊 탐색 결과 보고서]")
    
    # 예외 상황 처리: 만족하는 구역이 없을 때 [cite: 16, 25]
    if len(results) == 0:
        print("❌ 경고: 입력하신 조건을 만족하는 안전한 구조 구역이 없습니다.")
        print("위험도 제한을 높이거나 다른 특성을 입력해 주세요.")
        return

    print(f"✅ 진입 가능한 구역 총 {len(results)}곳을 발견했습니다.")
    print("-" * 45)
    print(f"{'ID':<4}{'구역 이름':<15}{'위험도':<6}{'소요시간':<6}{'특성'}")
    print("-" * 45)
    for s in results:
        print(f"{s[0]:<4}{s[1]:<15}{s[2]:<8}{s[3]:<8}{s[4]}")
    print("-" * 45)
    
    # 최적 경로 출력
    if best_sector:
        print(f"🚀 [최적 경로 안내] 가장 신속히 진입 가능한 구역은 '{best_sector[1]}'입니다.")
        print(f"⏱️ 예상 진입 소요 시간: {best_sector[3]}분 (위험도: {best_sector[2]}점)")
    print("=" * 45)

# 메인 실행 흐름
def main():
    show_robot_status()
    
    while True:  # 1. 반복문 시작
        print("\n[메뉴 선택] 1: 구역 추가 | 2: 최적 경로 탐색 | 3: 프로그램 종료")
        menu = input("▶️ 원하는 작업 번호를 입력하세요: ")
        
        if menu == "1":
            add_new_sector(sectors)
        elif menu == "2":
            # ... (탐색 코드 생략) ...
            pass
        elif menu == "3":  # 2. elif의 시작 위치가 위의 if, elif와 수직으로 맞아야 합니다.
            print("🤖 시스템을 종료합니다. 안전한 구조 활동을 지원합니다.")
            break  # 3. 이 break는 while문 안에 있으므로 정상 작동합니다!
        else:
            print("❌ 잘못된 입력입니다. 1, 2, 3 중 하나를 입력해 주세요.")