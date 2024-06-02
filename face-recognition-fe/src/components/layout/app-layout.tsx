import { Box, Container, Stack } from "@mui/material"

interface AppLayoutProps {
  children: React.ReactNode
}

const AppLayout: React.FC<AppLayoutProps> = ({ children }) => {
  return (
    <Stack minHeight={'100vh'}>
      <Box>
        <Container maxWidth="xl">

        </Container>
      </Box>
      <Stack position={'relative'}>
        {children}
      </Stack>
    </Stack>
  )
}

export default AppLayout