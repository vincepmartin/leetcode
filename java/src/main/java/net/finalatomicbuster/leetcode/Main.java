package net.finalatomicbuster.leetcode;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        System.out.println("Java based leetcode problems!");
        ArrayList<String> availableProblems = new ArrayList<>();

        availableProblems.add("751: CIDR Problem \"Easy\"");

        if(args.length < 1) {
            System.out.println("Supply a # or use \"list\" to get a list of all possible values.");
            return;
        }

        switch(args[0]) {
            case "751":
                LeetCode751 lc = new LeetCode751();
                lc.run();
                break;

            case "list":
                System.out.println("Available options: ");
                availableProblems.forEach( o -> {
                    System.out.println(o);
                });

            default:
                System.out.println("supply a # or use \"list\" to get a list of all possible values.");
        }
    }
}
