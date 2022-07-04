class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transformation = {}
        projected = {}
        for i in range(len(s)):
            origin = s[i]
            image = t[i]
            if origin in transformation:
                if transformation[origin] != image:
                    return False
            else:
                if projected.get(image):
                    return False
                transformation[origin] = image
                projected[image] = True
        return True