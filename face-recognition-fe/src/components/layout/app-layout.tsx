import { Box, Container, Stack } from "@mui/material";
import Header from "../header/header";

interface AppLayoutProps {
  children: React.ReactNode;
}

const AppLayout: React.FC<AppLayoutProps> = ({ children }) => {
  return (
    <Stack minHeight={"100vh"}>
      <Box>
        {/* <Container maxWidth="xl">
          <Header />
        </Container> */}
        <Header />
      </Box>
      <Stack position={"relative"} mt={"24px"}>
        {children}
      </Stack>
    </Stack>
  );
};

export default AppLayout;
