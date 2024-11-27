class Solution {
    public boolean containsDuplicate(int[] nums) {
       HashSet<Integer> samenumber=new HashSet<>();
        for(int num:nums){
            if(samenumber.contains(num)){
                return true;
            }
            samenumber.add(num);
        }
        return false;
    }
    
}
