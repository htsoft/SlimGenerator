<?php

declare(strict_types=1);

namespace App\Application\Actions\##TABLENAMECAP##;

use Psr\Http\Message\ResponseInterface as Response;

class ##TABLENAMECAP##ListAction extends ##TABLENAMECAP##Action
{
    /**
     * {@inheritdoc}
     */
    protected function action(): Response
    {
        $sortBy = $this->resolveArg('sortBy');
        $descending = (int) $this->resolveArg('descending');
        $startRow = (int) $this->resolveArg('startRow');
        $fetchCount = (int) $this->resolveArg('fetchCount');
        $filter = $this->resolveArg('filter');
        if ($filter == "%") {
            $filter = "";
        } else {
            $filter = urldecode($filter);
        }
        $this->logger->info("Filtered list for ##TABLENAMECAP## with filter: " . $filter . " sortby: " . $sortBy . " descending: " . $descending . " startrow: " . $startRow . " fetchcount: " . $fetchCount);
        $obj = $this->##TABLENAME##Repository->getSubset($filter, $sortBy, $descending, $startRow, $fetchCount);
        return $this->respondWithData($obj);
    }
}