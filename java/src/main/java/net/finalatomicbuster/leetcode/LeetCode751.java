package net.finalatomicbuster.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class LeetCode751 {

   public void run() {
      // Create some test data here.
      ipToCIDR("255.0.0.7", 10);
   }

   public List<String> ipToCIDR(String ip, int n) {
      // Convert the ip to a binary number.
      String[] ips = ip.split(Pattern.quote("."));

      // Get the whole binary representation of the binary number.

      for(String i: ips) {
         System.out.println(
            stringTo8BitBinary(i)
         );
      }

      // TODO: This is reasonably done, however, i think 0 is being converted to 0, not 00000000.
      Integer binary = Integer.parseInt(
              stringTo8BitBinary(ips[0]) +
              stringTo8BitBinary(ips[1]) +
              stringTo8BitBinary(ips[2]) +
              stringTo8BitBinary(ips[3]),2);

      Integer binary_second = binary + n-1;

      System.out.println(Integer.toBinaryString(binary));
      System.out.println(Integer.toBinaryString(binary_second));
      System.out.println(Integer.toBinaryString(binary & binary_second));


      List<String> returnValue = new ArrayList<>();
      return returnValue;
   }

   public String stringTo8BitBinary(String num) {
      String binary = Integer.toBinaryString(Integer.valueOf(num, 2));
      Integer zerosNeeded = 8 - binary.length();
      StringBuilder prefix = new StringBuilder();

      for(int i = 0; i < zerosNeeded; i ++ ) {
         prefix.append("0");
      }

      return prefix.toString() + binary;

   }

}
