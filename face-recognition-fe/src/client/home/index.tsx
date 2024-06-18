"use client";

import {
  Box,
  Container,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from "@mui/material";
import Link from "next/link";

interface HomeProps {}

const Home: React.FC<HomeProps> = (props) => {
  return (
    <Container maxWidth="xl">
      <Typography
        sx={{
          fontSize: "36px",
          fontWeight: "600",
          textAlign: "center",
        }}
      >
        All users
      </Typography>
      <Box>
        <Link href={"/attendance"}>Check attendance</Link>
      </Box>
      <Box>
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 700 }}>
            <TableHead>
              <TableRow>
                <TableCell>No</TableCell>
                <TableCell>Fullname</TableCell>
                <TableCell>Date of Birth</TableCell>
                <TableCell>Address</TableCell>
                <TableCell>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              <TableRow>
                <TableCell>1</TableCell>
                <TableCell>Trần Bảo Trung</TableCell>
                <TableCell>06/09/2003</TableCell>
                <TableCell>Hanoi</TableCell>
                <TableCell>Edit</TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </Container>
  );
};

export default Home;
