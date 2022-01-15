class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split(".")
        v2_list = version2.split(".")
        v1_len = len(v1_list)
        v2_len = len(v2_list)
        if(v1_len > v2_len):
            for i in range(v1_len - v2_len):
                v2_list.append("0")
        elif(v2_len > v1_len):
            for i in range(v2_len - v1_len):
                v1_list.append("0")
        for i in range(len(v1_list)):
            string1 = v1_list[i].lstrip("0")
            string2 = v2_list[i].lstrip("0")
            if(string1 == ""):
                string1 = "0"
            if(string2 == ""):
                string2 = "0"
            if(int(string1) > int(string2)):
                return 1
            elif(int(string1)<int(string2)):
                return -1
        return 0