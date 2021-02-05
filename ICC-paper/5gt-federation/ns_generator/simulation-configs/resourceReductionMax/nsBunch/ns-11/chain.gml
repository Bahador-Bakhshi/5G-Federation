graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 12
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 14
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 4
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 77
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 137
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 128
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 182
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 69
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 191
  ]
]
