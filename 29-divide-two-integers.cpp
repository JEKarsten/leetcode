class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) return 0;
        
        long dividendA = abs(dividend);
        long divisorA = abs(divisor);
        
        long result = 0;
        
        while (dividendA >= divisorA) {
            int shiftCounter = 0;
            cout << dividendA << endl;
            while (dividendA >= (divisorA << shiftCounter)) {
                shiftCounter++;
            }
            result += 1 << (shiftCounter - 1);
            dividendA -= divisorA << (shiftCounter - 1);
        }
        
        if ((dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0)) {
            if (result == -2147483648) result = 2147483647;
            return (int) result;
        }
        else {
            if (result == 2147483648) return 2147483647;
            return (int) -result;
        }
    }
};