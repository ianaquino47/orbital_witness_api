import {
  FormControl,
  FormLabel,
  HStack,
  VStack,
  Input,
  Radio,
  RadioGroup,
  Box,
} from "@chakra-ui/react";
import React from "react";

const FilterSettings = ({ params, setParams, setTitleClass }) => {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setParams({
      ...params,
      [name]: value.replace(/\s/g, ""),
    });
  };
  return (
    <VStack spacing="12px" align="center">
      <Box>
        <FormControl>
          <RadioGroup onChange={setTitleClass} defaultValue="all">
            <HStack spacing="24px">
              <Radio value="all">All</Radio>
              <Radio value="freehold">Freehold</Radio>
              <Radio value="leasehold">Leasehold</Radio>
            </HStack>
          </RadioGroup>
        </FormControl>
      </Box>
      <HStack>
        <FormControl>
          <FormLabel>Sort by</FormLabel>
          <Input
            maxWidth="sm"
            name="sortParams"
            value={params.sortParams}
            onChange={handleChange}
            placeholder="sort by values separated by comma"
            size="sm"
          />
        </FormControl>
        <FormControl>
          <FormLabel>Order by</FormLabel>
          <Input
            name="orderParams"
            maxWidth="sm"
            value={params.orderParams}
            onChange={handleChange}
            placeholder="order by values separated by comma"
            size="sm"
          />
        </FormControl>
        <FormControl>
          <FormLabel>Page</FormLabel>
          <Input
            maxWidth="sm"
            name="page"
            value={params.page}
            onChange={handleChange}
            size="sm"
          />
        </FormControl>
        <FormControl>
          <FormLabel>Limit per page</FormLabel>
          <Input
            name="limitPerpage"
            maxWidth="sm"
            value={params.limitPerpage}
            onChange={handleChange}
            size="sm"
          />
        </FormControl>
      </HStack>
    </VStack>
  );
};
export default FilterSettings;
