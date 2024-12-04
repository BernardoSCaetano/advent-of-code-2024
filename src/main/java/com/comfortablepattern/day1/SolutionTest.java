package com.comfortablepattern.day1;

import org.junit.jupiter.api.Test;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    @Test
    void testTotalDistance_case() throws IOException {

        // Set the file path for the program

        // Run the test
        int result = Solution.getTotalDistanceBetweenLists();

        // Assert the result
        assertEquals(1223326, result);
    }

    @Test
    void testSimilarityScore_case() throws IOException {
        // Run the test
        int result = Solution.getSimilarityScore();

        // Assert the result
        assertEquals(21070419, result);
    }
}
