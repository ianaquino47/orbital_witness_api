import { Card, CardBody, CardHeader } from "@chakra-ui/card";
import { Box, Heading, Stack, StackDivider, Text } from "@chakra-ui/layout";
import React from "react";

const TitleCard = ({ title }) => {
  return (
    <Card
      maxW="sm"
      bg={title.title_class === "Freehold" ? "#EDF2F7" : "#A0AEC0"}
    >
      <CardHeader height="80px">
        <Heading size="md">Title No. {title?.title_number}</Heading>
      </CardHeader>
      <CardBody>
        <Stack divider={<StackDivider />} spacing="4">
          <Box>
            <Heading size="xs" textTransform="uppercase">
              ID
            </Heading>
            <Text pt="2" fontSize="sm">
              {title?.id}
            </Text>
          </Box>
          <Box>
            <Heading size="xs" textTransform="uppercase">
              Title Class
            </Heading>
            <Text pt="2" fontSize="sm">
              {title?.title_class}
            </Text>
          </Box>
          {title.content && (
            <Box>
              <Heading size="xs" textTransform="uppercase">
                Content
              </Heading>
              <Text pt="2" fontSize="sm">
                {title?.content}
              </Text>
            </Box>
          )}
        </Stack>
      </CardBody>
    </Card>
  );
};

export default TitleCard;
