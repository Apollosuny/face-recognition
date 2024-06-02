'use client'

import { usePathname } from "next/navigation"
import { useMemo } from "react"
import AdminLayout from "./admin-layout"
import AppLayout from "./app-layout"

interface LayoutProps {
  children: React.ReactNode
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const pathName = usePathname()
  const isAdmin = useMemo(() => pathName.includes('/admin'), [pathName])

  return (
    isAdmin ? <AdminLayout>
      {children}
    </AdminLayout> : <AppLayout>
      {children}
    </AppLayout>
  )
}

export default Layout