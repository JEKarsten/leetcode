class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size(), target);
    }

private:
    int binarySearch(vector<int>& nums, int i, int j, int target) {
        if (i == j or nums[i] > target) return i;
        int midpoint = (i + j) / 2;
        if (nums[midpoint] == target) return midpoint;
        if (nums[midpoint] > target) {
            return binarySearch(nums, i, midpoint, target);
        } else {
            return binarySearch(nums, midpoint + 1, j, target);
        }
    }
};