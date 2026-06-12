# 1. 재난 구역 데이터 정의 (2차원 리스트)
sectors = [
]

def show_all_sectors(sector_list):
    """현재 데이터베이스에 등록된 모든 재난 구역을 출력하는 함수"""
    print("\n[📋 현재 등록된 모든 재난 구역 목록]")
    print("-" * 45)
    print(f"{'ID':<4}{'구역 이름':<15}{'위험도':<6}{'소요시간':<6}{'특성'}")
    print("-" * 45)
    
    # 2차원 리스트의 모든 행을 하나씩 꺼내어 출력합니다.
    for s in sector_list:
        print(f"{s[0]:<4}{s[1]:<15}{s[2]:<8}{s[3]:<8}{s[4]}")
        
    print("-" * 45)

def add_new_sector(sector_list):
    """사용자로부터 새로운 재난 구역 정보를 입력받아 리스트에 추가하는 함수"""
    print("\n[➕ 새로운 재난 구역 추가]")
    
    # 새로운 구역 ID 계산
    next_id = sector_list[-1][0] + 1 if len(sector_list) > 0 else 1
    
    name = input("▶️ 구역 이름을 입력하세요 (예: G-2 대피소): ")
    
    try:
        risk = int(input("▶️ 위험도 점수를 입력하세요 (0~100): "))
        time = int(input("▶️ 진입 소요 시간(분)을 입력하세요: "))
    except ValueError:
        print("❌ 위험도와 소요 시간은 숫자로 입력해야 합니다. 추가를 취소합니다.")
        return
        
    while True:
        user_condition = input("▶️ 선호하는 구역 특성을 입력하세요 (통신가능 / 붕괴위험 / 가스누출 / 안전): ")
    
    # 사용자가 입력한 값이 정해진 3개의 카테고리 안에 있는지 확인합니다.
        if user_condition in ["통신가능", "붕괴위험", "가스누출", "안전"]:
            break  # 올바르게 입력했으므로 반복문을 탈출합니다.
        else:
            print("❌ 잘못된 특성입니다. '통신가능', '붕괴위험', '가스누출', '안전' 중 하나를 정확히 입력해 주세요.")
    
    new_sector = [next_id, name, risk, time, user_condition]
    sector_list.append(new_sector)  # 깔끔하게 수정 완료!
    print(f"✅ '{name}' 구역이 성공적으로 데이터베이스에 등록되었습니다!")

def show_robot_status():
    """로봇의 현재 시스템 상태를 안내하는 함수"""
    print("=" * 45)
    print("🤖 재난 구조 로봇 경로 탐색 시스템 활성화")
    print("=" * 45)

def search_safe_sectors(sector_list, max_risk, max_time, condition): # 💡 max_time 매개변수 추가
    """위험도 점수 이하, 소요시간 이하, 특성 조건이 모두 맞는 구역을 필터링하는 함수"""
    filtered_list = []
    for sector in sector_list:
        # 💡 sector[3](소요시간)이 max_time 이하인지 검사하는 조건을 and로 연결합니다!
        if sector[2] <= max_risk and sector[3] <= max_time and sector[4] == condition:
            filtered_list.append(sector)
    return filtered_list

def find_best_sector(filtered_list):
    """필터링된 구역 중 이동 소요 시간이 가장 짧은 최적 구역을 찾는 함수"""
    if len(filtered_list) == 0:
        return None
    best = filtered_list[0]
    for sector in filtered_list:
        if sector[3] < best[3]:
            best = sector
    return best

def print_report(results, best_sector):
    """최종 탐색 결과를 출력하는 함수"""
    print("\n[📊 탐색 결과 보고서]")
    
    if len(results) == 0:  # 깔끔하게 수정 완료!
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
    
    if best_sector:
        print(f"🚀 [최적 경로 안내] 가장 신속히 진입 가능한 구역은 '{best_sector[1]}'입니다.")
        print(f"⏱️ 예상 진입 소요 시간: {best_sector[3]}분 (위험도: {best_sector[2]}점)")
    print("=" * 45)

# 메인 실행 흐름
def main():
    show_robot_status()
    
    while True:
        print("\n[메뉴 선택] 1: 구역 추가 | 2: 최적 경로 탐색 | 3: 모든 구역 조회 | 4: 프로그램 종료")
        menu = input("▶️ 원하는 작업 번호를 입력하세요: ")
        
        if menu == "1":
            add_new_sector(sectors)
        elif menu == "2":
            try:
                user_risk = int(input("\n▶️ 로봇이 진입할 수 있는 최대 허용 위험도를 입력하세요 (0~100): "))
                user_time = int(input("▶️ 로봇이 이동할 수 있는 최대 허용 소요시간(분)을 입력하세요: "))
            except ValueError:
                print("❌ 숫자로 입력해야 합니다.")
                continue
                
            user_condition = input("▶️ 선호하는 구역 특성을 입력하세요 (통신가능 / 붕괴위험 / 가스누출 / 안전): ")
            
            filtered = search_safe_sectors(sectors, user_risk, user_time, user_condition)
            best = find_best_sector(filtered)
            print_report(filtered, best)
        elif menu == "3":
            show_all_sectors(sectors)
        elif menu == "4":
            print("🤖 시스템을 종료합니다. 안전한 구조 활동을 지원합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 1, 2, 3 중 하나를 입력해 주세요.")

if __name__ == "__main__":
    main()