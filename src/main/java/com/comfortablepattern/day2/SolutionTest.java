package com.comfortablepattern.day2;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    @Test
    void testGetNumberOfSafeReports() throws IOException {

        List<List<Integer>> reports = Solution.readInput();


        // Run the test
        int result = Solution.getNumberOfSafeReports(reports,
                new Solution.NormalReportCheckStrategy());

        // Assert the result
        assertEquals(246, result);
    }

    @Test
    void testGetNumberOfSafeReportsWithDampener() throws IOException {
        List<List<Integer>> reports = Solution.readInput();

        // Run the test
        int result = Solution.getNumberOfSafeReports(reports,
                new Solution.DampenerReportCheckStrategy());

        // Assert the result
        assertEquals(318, result);
    }
}
