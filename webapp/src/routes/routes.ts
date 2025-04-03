import { RouteObject } from "react-router";
import { Home } from "../page";
import { Result } from "../page/Result";

export const routes: RouteObject[] = [
    {
        index: true,
        path: '/',
        Component: Home,
    },
    {
        path: '/result',
        Component: Result,
    }
];