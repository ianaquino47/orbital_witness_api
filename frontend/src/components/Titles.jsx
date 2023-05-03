import { Box, SimpleGrid } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";
import TitleCard from "./TitleCard";

export const Titles = ({ titles, titleLimit }) => {
  return (
    <Box>
      <SimpleGrid columns={[2, 3, 4]} gap={6}>
        {titles?.slice(0, titleLimit).map((title) => (
          <Box key={title.id}>
            <Link
              to={`titles/${title.id}`}
              style={{ textDecoration: "none", color: "black" }}
            >
              <TitleCard title={title} />
            </Link>
          </Box>
        ))}
      </SimpleGrid>
    </Box>
  );
};
