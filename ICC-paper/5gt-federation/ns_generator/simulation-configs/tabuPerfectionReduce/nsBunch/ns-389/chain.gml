graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 4
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 1
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 3
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 172
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 171
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 147
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 169
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 78
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 155
  ]
]
