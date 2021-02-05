graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 5
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 9
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 12
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 129
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 140
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 155
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 131
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 97
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 103
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 103
  ]
]
