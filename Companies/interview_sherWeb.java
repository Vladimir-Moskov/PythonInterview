
class Solution {
   static public String solution(String S) {
        if (S.isEmpty() ) {
            return "";
        }
        // write your code in Java SE 8
        char [] char_ar = new char[S.length()];
        int k = 0;
        for (int i = 0; i < S.length(); i++){
            if (S.charAt(i) != ' ' &&  S.charAt(i) != '-'){
                char_ar[k] = S.charAt(i);
                k ++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < char_ar.length; i++){
        	if ( char_ar[i] != '\0') {
        		 sb.append(char_ar[i]);
                 if ((i + 1)% 3 == 0 && i != (char_ar.length - 1)){
                     sb.append("-");
                 }
        	}

        }

        return sb.toString();

    }
}
static public int solution2(int[] A) {
		int result = 0;

		Hashtable<Integer, Integer> val_counter = new Hashtable<Integer, Integer>();
		for (int i = 0; i < A.length; i++) {
			if (val_counter.containsKey(A[i])){
				val_counter.put(A[i], val_counter.get(A[i]) + 1);
			}
			else {
				val_counter.put(A[i], 1);
			}
		}
		Iterator<Map.Entry<Integer, Integer>> iterator = val_counter
				.entrySet().iterator();


		//iterate using while loop
		while( iterator.hasNext() ){
			if (result < 1000000000)
			  {
				   Map.Entry<Integer, Integer> entry = iterator.next();
				   int factorial = 0;
				   int v = entry.getValue();
				   if (v > 1) {
					   combination = 1;
		        	   for (int i = 3; i <= v; i ++) {
		        		   combination = combination + (i - 1);
		        	   }
		           }

				   result += combination;
			   }

		}



		return result;

    }