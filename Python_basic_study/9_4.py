class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 공격 방향
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력

    def damaged(self, damage): # damage 만큼 유닛 피해
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
        self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
        if self.hp <= 0: # 남은 체력이 0 이하이면?
            print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리

# 파이어뱃 : 공격 유닛, 화염방사기. 
firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 체력 0