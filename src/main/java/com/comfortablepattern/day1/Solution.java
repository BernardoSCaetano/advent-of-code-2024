package com.comfortablepattern.day1;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {


    private static final String FILE_PATH = "src/main/java/com/comfortablepattern/day1/input.txt";

    public static void main(String[] args) throws IOException {
        System.out.println(getTotalDistanceBetweenLists()); // Output the total distance
        System.out.println(getSimilarityScore()); // Output the similarity score
    }

    // Method to read input from a file and parse into two lists
    public static List<List<Integer>> readInput() throws IOException {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] numbers = line.split("\\s+");
                list1.add(Integer.parseInt(numbers[0]));
                list2.add(Integer.parseInt(numbers[1]));
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        result.add(list1);
        result.add(list2);
        return result;
    }

    // Method to count occurrences of each element in a list
    public static Map<Integer, Long> countOccurrences(List<Integer> list) {
        return list.stream()
                .collect(Collectors.groupingBy(e -> e, Collectors.counting()));
    }

    // Method to calculate total distance between lists
    public static int getTotalDistanceBetweenLists() throws IOException {
        List<List<Integer>> inputLists = readInput();
        List<Integer> list1 = inputLists.get(0);
        List<Integer> list2 = inputLists.get(1);

        Collections.sort(list1);
        Collections.sort(list2);

        int diffSum = 0;
        for (int i = 0; i < list1.size(); i++) {
            diffSum += Math.abs(list1.get(i) - list2.get(i));
        }

        return diffSum;
    }

    // Method to calculate similarity score
    public static int getSimilarityScore() throws IOException {
        List<List<Integer>> inputLists = readInput();
        List<Integer> list1 = inputLists.get(0);
        List<Integer> list2 = inputLists.get(1);

        Collections.sort(list1);

        Map<Integer, Long> counterList2 = countOccurrences(list2);

        int similaritySum = 0;
        for (int value : list1) {
            similaritySum += value * counterList2.getOrDefault(value, 0L);
        }

        return similaritySum;
    }
}
