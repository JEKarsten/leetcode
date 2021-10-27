class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int len = nums.size();
        if (len == 0) return {-1, -1};
        
        int left = leftBinarySearch(nums, 0, len - 1, target);
        int right = rightBinarySearch(nums, 0, len - 1, target);
        return {left, right};
    }

private:
    int leftBinarySearch(vector<int>& nums, int left, int right, int target) {
        if (left > right) return -1;
        if (left == right) {
            if (nums[left] == target) return left;
            return -1;
        }
        
        int midpoint = (left + right) / 2;
        if (nums[midpoint] < target) {
            return leftBinarySearch(nums, midpoint + 1, right, target);
        } else {
            return leftBinarySearch(nums, left, midpoint, target);
        }
    }
    
    int rightBinarySearch(vector<int>& nums, int left, int right, int target) {
        if (left > right) return -1;
        if (left == right) {
            if (nums[left] == target) return left;
            if (nums[left] > target and left > 0 and nums[left - 1] == target) return left - 1;
            return -1;
        }
        
        int midpoint = (left + right) / 2;
        if (nums[midpoint] <= target) {
            return rightBinarySearch(nums, midpoint + 1, right, target);
        } else {
            return rightBinarySearch(nums, left, midpoint, target);
        }
    }
};