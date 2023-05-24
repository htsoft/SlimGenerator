<?php

declare(strict_types=1);

namespace App\Application\Actions\##TABLENAMECAP##;

use Psr\Http\Message\ResponseInterface as Response;

class ##TABLENAMECAP##CountAction extends ##TABLENAMECAP##Action
{
    /**
     * {@inheritdoc}
     */
    protected function action(): Response
    {
        $filter = $this->resolveArg('filter');
        if ($filter == "%") {
            $filter = "";
        } else {
            $filter = urldecode($filter);
        }
        $this->logger->info("Requested total count for ##TABLENAMECAP## with filter: " . $filter);
        $numero = $this->##TABLENAME##Repository->getCount($filter);
        return $this->respondWithData($numero);
    }
}