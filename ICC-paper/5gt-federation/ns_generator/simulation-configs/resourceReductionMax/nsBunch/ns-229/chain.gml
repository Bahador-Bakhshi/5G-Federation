graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 1
    memory 5
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 1
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 159
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 131
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 83
  ]
  edge [
    source 0
    target 3
    delay 33
    bw 58
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 160
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 81
  ]
]
