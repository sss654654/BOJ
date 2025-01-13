'''
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''
import sys

N = int(sys.stdin.readline()) # 3*2^k

def star(n):
    if n == 3:
        return ["  *  ", " * * ","*****"]
    tmp = star(n//2)
    stars = []
    for i in tmp:
        stars.append(" "*(n//2)+i+" "*(n//2))
    for i in tmp:
        stars.append(i+" "+i)
    return stars
result = star(N)
for i in range(len(result)):
    print(result[i])
    
'''
3
  *  (2)                      
 * * (1)                   
*****(0)

6
     *     (5)                        
    * *    (4)                      
   *****   (3)                      
  *     *  (2)                    
 * *   * * (1)                  
***** *****(0)

12
           * (11)                       
          * *                       
         *****                      
        *     *                     
       * *   * *                    
      ***** *****                   
     *           *                  
    * *         * *                 
   *****       *****                
  *     *     *     *               
 * *   * *   * *   * *              
***** ***** ***** *****

예제 입력 1 
24
예제 출력 1 
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****
'''