<?php

declare(strict_types=1);

namespace App\Application\Actions\##TABLENAMECAP##;

use Psr\Http\Message\ResponseInterface as Response;

class ##TABLENAMECAP##ListAllAction extends ##TABLENAMECAP##Action
{
    /**
     * {@inheritdoc}
     */
    protected function action(): Response
    {
        $this->logger->info("List all for ##TABLENAMECAP##");
        $obj = $this->##TABLENAME##Repository->getAll();
        return $this->respondWithData($obj);
    }
}