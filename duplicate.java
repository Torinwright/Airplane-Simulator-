package duplicator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map; 
import java.util.Map.Entry; 
import java.util.Set;


public class duplicate {
	public static void main(String args[]) {
		
		String[] names = { "Torin", "Tim","Timmy","Tom","Timmy", "Timmy"};
		
		System.out.println("Finding duplicate elements in array");
		for (int i = 0; i < names.length; i++) {
			for (int j = i + 1; j < names.length; j++) {
				if (names[i].equals(names[j])) {
					
				}
			}
		}
		
		
		

		
		
		Map<String, Integer> nameAndCount = new HashMap<>();
		
		for (String name : names) { 
			Integer count = nameAndCount.get(name); 
			if (count == null) {
				nameAndCount.put(name, 1); 
			} 
			else { nameAndCount.put(name, ++count);
			} 
			}

		Set<Entry<String, Integer>> entrySet = nameAndCount.entrySet();
		for (Entry<String, Integer> entry : entrySet) {
			if (entry.getValue() > 1 ) {
				System.out.println("Duplicate element from array : " + entry.getKey());
				
				}
			
			if (entry.getValue() <= 1 ) {
				System.out.println("There are no duplicates");
			}
			if (entry.getValue() > 2) {
				System.out.println(entry.getKey() +" has more than 2 copies");
			}
			
			
			}
				
			

		
		
	}

}
