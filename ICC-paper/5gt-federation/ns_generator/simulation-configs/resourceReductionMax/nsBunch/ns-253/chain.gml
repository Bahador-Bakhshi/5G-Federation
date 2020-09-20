graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 5
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 189
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 62
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 113
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 65
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 102
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 69
  ]
]
