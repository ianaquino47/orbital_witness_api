import { Box, Center } from "@chakra-ui/layout";
import React, { useEffect, useState } from "react";
import { Button } from "@chakra-ui/button";
import { Text, Spinner, VStack } from "@chakra-ui/react";
import FilterSettings from "./FilterSettings";
import { Titles } from "./Titles";

const MainPage = () => {
  const [data, setData] = useState();
  const [titleClass, setTitleClass] = useState("all");
  const [params, setParams] = useState({
    orderParams: "",
    sortParams: "",
    page: 1,
    limitPerpage: 10,
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch("http://localhost:8000/api/titles")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((json) => {
        const { data } = json;
        setData(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching data");
      });
  }, []);

  const getUrl = (
    filter_params,
    sort_params,
    order_params,
    page,
    limitPerpage
  ) => {
    let params_array = [];
    [filter_params, sort_params, order_params, page, limitPerpage].forEach(
      (param) => {
        if (!!param) {
          params_array.push(param);
        }
      }
    );
    const params = params_array.join("&");

    const url = `/${!!params ? "?" : ""}${params}`;

    return url;
  };

  const handleSubmit = () => {
    const hasFilter = titleClass !== "all";
    const filter_params = hasFilter ? `title_class=${titleClass}` : "";
    const sort_params = params.sortParams ? `_sort=${params.sortParams}` : "";
    const order_params = params.orderParams
      ? `_order=${params.orderParams}`
      : "";
    const page = params.page ? `_page=${params.page}` : "";
    const limit_per_page = params.limitPerpage
      ? `_limit=${params.limitPerpage}`
      : "";

    const url = getUrl(
      filter_params,
      sort_params,
      order_params,
      page,
      limit_per_page
    );

    setLoading(true);

    fetch(`http://localhost:8000/api/titles${url}`)
      .then((response) => {
        if (response.ok) {
          setError("");
          return response.json();
        }
        return response.json().then((res) => {
          setError(res.message);
          throw new Error(res.message);
        });
      })
      .then((json) => {
        const { data } = json;
        setData(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err.message);
        setLoading(false);
      });
  };

  return (
    <Box>
      <VStack>
        <FilterSettings
          params={params}
          setParams={setParams}
          setTitleClass={setTitleClass}
        />
        {error && (
          <Text sx={{ color: "red" }} fontSize="sm">
            {error}
          </Text>
        )}
        <Button
          isLoading={loading}
          spinner={<Spinner size={"sm"} />}
          onClick={handleSubmit}
        >
          Get Titles
        </Button>
        {loading ? (
          <Center pos="absolute" height="100vh">
            <Spinner />
          </Center>
        ) : (
          <Titles titles={data} titleLimit={params.limitPerpage} />
        )}
      </VStack>
    </Box>
  );
};

export default MainPage;
