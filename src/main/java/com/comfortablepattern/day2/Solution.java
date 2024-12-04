package com.comfortablepattern.day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Solution {


    private static final String FILE_PATH = "src/main/java/com" +
            "/comfortablepattern/day2/input.txt";

    public static void main(String[] args) throws IOException {
        List<List<Integer>> levels = readInput();

        System.out.println(getNumberOfSafeReports(levels, new NormalReportCheckStrategy())); // 403
        System.out.println(getNumberOfSafeReports(levels,
                new DampenerReportCheckStrategy())); // 318
    }

    /**
     * Reads the input from a file and parses it into a list of lists of integers.
     * The input file contains many reports, one report per line.
     * Each report is a list of numbers called levels that are separated by spaces.
     *
     * @return a list of lists of integers representing the parsed input
     * @throws IOException if an I/O error occurs reading from the file
     */
    public static List<List<Integer>> readInput() throws IOException {

        List<List<Integer>> result = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            String line;
            while ((line = reader.readLine()) != null) {
                List<Integer> report = new ArrayList<>();
                String[] reportAsStringArray = line.split(" ");
                for (String level : reportAsStringArray) {
                    report.add(Integer.parseInt(level));
                }
                result.add(report);
            }
        }

        return result;
    }


    /**
     * For each report in the given list of reports, determines if it is safe
     * according to the given strategy.
     *
     * @param reports  A list of reports, where each report is a list of integers.
     * @param strategy A strategy to determine if a report is safe.
     * @return The number of safe reports according to the given strategy.
     */
    public static int getNumberOfSafeReports(List<List<Integer>> reports,
                                             ReportCheckStrategy strategy) {
        int safeReportCounter = 0;

        for (List<Integer> report : reports) {
            if (strategy.isReportSafe(report)) {
                safeReportCounter++;
            }
        }

        return safeReportCounter;
    }

    /**
     * Interface for a strategy to determine if a report is safe.
     */
    public interface ReportCheckStrategy {
        boolean isReportSafe(List<Integer> report);
    }

    /**
     * PROBLEM 1: Normal Report Check Strategy
     */
    public static class NormalReportCheckStrategy implements ReportCheckStrategy {
        @Override
        public boolean isReportSafe(List<Integer> report) {
            // For each report, check if levels are ordered ascendingly or
            // descendingly, return true if so, false otherwise, and they can't be equal
            boolean isAscending = true;
            boolean isDescending = true;

            if (report.size() < 2) {
                return true;
            }

            for (int i = 1; i < report.size(); i++) {
                Integer currentLevel = report.get(i);
                Integer levelBefore = report.get(i - 1);
                if (Math.abs(currentLevel - levelBefore) > 3) {
                    return false;
                } else if (currentLevel > levelBefore) {
                    isDescending = false;
                } else if (currentLevel < levelBefore) {
                    isAscending = false;
                } else {
                    return false;
                }
            }
            return isAscending || isDescending;
        }
    }

    /**
     * PROBLEM 2: Dampener Report Check Strategy
     */
    public static class DampenerReportCheckStrategy implements ReportCheckStrategy {
        @Override
        public boolean isReportSafe(List<Integer> report) {
            // Check if the report is already safe
            if (isOrdered(report)) {
                return true;
            }

            // Attempt to remove each element and check if the remaining report is safe
            for (int i = 0; i < report.size(); i++) {
                List<Integer> modifiedReport = new ArrayList<>(report);
                modifiedReport.remove(i); // Remove the current element
                if (isOrdered(modifiedReport)) {
                    return true; // The report is safe after removing this level
                }
            }

            return false; // No single removal can make the report safe
        }

        /**
         * Helper method to check if a list is ordered (ascending or descending)
         * with differences between consecutive levels ≤ 3.
         *
         * @param report The list of levels.
         * @return True if the list is ordered, false otherwise.
         */
        private boolean isOrdered(List<Integer> report) {
            if (report.size() < 2) {
                return true; // Any list with fewer than 2 levels is considered safe
            }

            boolean isAscending = true;
            boolean isDescending = true;

            for (int i = 1; i < report.size(); i++) {
                int currentLevel = report.get(i);
                int previousLevel = report.get(i - 1);

                if (Math.abs(currentLevel - previousLevel) > 3) {
                    return false; // Difference between consecutive levels is too large
                }

                if (currentLevel > previousLevel) {
                    isDescending = false; // Violates descending order
                } else if (currentLevel < previousLevel) {
                    isAscending = false; // Violates ascending order
                } else {
                    return false; // Equal levels are not allowed
                }
            }

            return isAscending || isDescending;
        }
    }


}
