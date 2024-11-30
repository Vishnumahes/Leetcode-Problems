class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer>number=new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(number.contains(nums[i])){
                return true;
            }
            number.add(nums[i]);
            if(number.size()>k){
                number.remove(nums[i-k]);
            }
            }
             return false;
            }
            
            }
       
        
        
    
