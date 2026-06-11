class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. Warden ka register banaya (Khaali Dictionary)
        warden_register = {}  # Ismein data aise dikhega -> {number: index}
        
        # 2. Loop chalayenge jo index (i) aur number (num) dono ek saath dega
        for i, num in enumerate(nums):
            
            # 3. Humhe kis number ki talaash hai?
            required_number = target - num
            
            # 4. Warden se pucho: "Kya register mein required_number pehle se hai?"
            if required_number in warden_register:
                # Agar haan, toh purane number ka index aur current index return kar do
                return [warden_register[required_number], i]
            
            # 5. Agar nahi mila, toh current number aur uske index ko register mein note kar lo
            warden_register[num] = i