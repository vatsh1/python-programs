import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String targetString = sc.nextLine();
        int sampleStringCount = Integer.parseInt(sc.nextLine());
        List<String> sampleStrings = new ArrayList<>();
        for (int i = 0; i < sampleStringCount; i++) {
            String input = sc.nextLine();
            sampleStrings.add(input);
        }
//        # target_string = "dogisaloyalanimal"
//    # sample_strings = ["a", "alloy", "is", "god", "lamina"]

        String joinedString = String.join("", sampleStrings);

        /* check for the length of the string */
        if (targetString.length() != joinedString.length()) {
            System.out.println("NO");
        } else {
            HashMap<String, Integer> targetMap = new HashMap<String, Integer>();
            /* create a map of characters in the Target String */
            for (int i = 0; i < targetString.length(); i++) {
                String character = Character.toString(targetString.charAt(i));
                if (targetMap.containsKey(character)) {
                    targetMap.put(character, targetMap.get(character) + 1);
                } else {
                    targetMap.put(character, 1);
                }
            }

            /* compare it with the characters in the Sample Strings */

            for (int i = 0; i < joinedString.length(); i++) {
                String character = Character.toString(joinedString.charAt(i));
                if (!targetMap.containsKey(character)) {
                    System.out.println("NO");
                    return;
                } else {
                    targetMap.put(character, targetMap.get(character) - 1);
                    if (targetMap.get(character) == 0) {
                        targetMap.remove(character);
                    }
                }
            }

            /* check the size if the target map */
            if (targetMap.size() == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}