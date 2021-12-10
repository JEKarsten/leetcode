class Solution {
    public int reverse(int x) {
        int output = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (output > Integer.MAX_VALUE/10 || (output == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (output < Integer.MIN_VALUE/10 || (output == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            output = output * 10 + pop;
        }
        return output;
    }
}