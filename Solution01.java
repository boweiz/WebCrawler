
public class Solution01 {

	public static boolean isUniqueChar(String s) {
		// assume characters in the String are ASCII, the principle works under other situations
		
		// since there are 256 possible unique characters, str.length is big than that will return false
		if(s.length() > 256) return false;
		
		// build a boolean[256] to set every character in String as true
		boolean[] set = new boolean[256];
		
		for(int i=0; i<s.length(); i++) {
			
			int index = s.charAt(i);
			// if for a certain set[index], its value have already been set true, then it is not unique.
			if(set[index]) return false;
			set[index] = true;
					
