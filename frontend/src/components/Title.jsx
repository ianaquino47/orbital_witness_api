import { Center } from "@chakra-ui/layout";
import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { Spinner } from "@chakra-ui/react";
import TitleCard from "./TitleCard";

const Title = () => {
  const [data, setData] = useState();
  const [loading, setLoading] = useState(true);
  const params = useParams();

  useEffect(() => {
    fetch(`http://localhost:8000/api/titles/${params.id}`)
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
  }, [params.id]);

  return (
    <div>
      {loading ? (
        <Center height="100vh">
          <Spinner />
        </Center>
      ) : (
        <>
          <Link to="/">Go back to all Titles</Link>
          <Center minHeight="100vh">
            <TitleCard title={data} />
          </Center>
        </>
      )}
    </div>
  );
};

export default Title;
