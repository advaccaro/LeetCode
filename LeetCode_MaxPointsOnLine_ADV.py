# LeetCode - Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/description/
# Adam Vaccaro



# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.


from fractions import gcd

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        sorted_xs = sorted(points,key= lambda r: r.x)
        sorted_ys = sorted(points,key= lambda r: r.y)
        my_dict = dict()
        max_ct = 0
        for ind,point in enumerate(sorted_xs):
            print(ind)
            for point2 in sorted_xs:#[ind:]:
                try:
                    #slope = (point.y-point2.y)/(point.x-point2.x)
                    #intercept = point.y - slope*point.x
                    num = point2.y - point.y
                    den = point2.x - point.x
                    gcdizzle = gcd(num,den)
                    #dummy = Fraction()
                    top = num//gcdizzle
                    bot = den//gcdizzle
                except ZeroDivisionError:
                    top = point2.y - point.y
                    bot = point2.x - point.x
                    #slope = float("Inf")
                    
                    #intercept = point.x
                except Exception as e:
                    print(e)
                #key = (slope,intercept)
                if bot < 0:
                    bot = bot * -1
                    top = top * -1
                key = (top,bot,point)
                my_dict[key] = my_dict.get(key,set())
                my_dict[key].add(point)
                my_dict[key].add(point2)
                
                if len(my_dict[key]) > max_ct:
                    max_ct = len(my_dict[key])
                
                #else:
                 #   for pt in [point, point2]:
                #if my_dict[key] is None:
                    
        if (len(my_dict.values()) == 0): 
            my_answer = 0
        else:
            my_answer = len(max(my_dict.values()))
        return (max_ct)