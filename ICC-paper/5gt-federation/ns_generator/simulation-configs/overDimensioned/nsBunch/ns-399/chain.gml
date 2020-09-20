graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 15
    bw 0
  ]
  edge [
    source 0
    target 1
    delay 15
    bw 0
  ]
  edge [
    source 1
    target 2
    delay 15
    bw 0
  ]
  edge [
    source 1
    target 3
    delay 15
    bw 0
  ]
  edge [
    source 2
    target 5
    delay 15
    bw 0
  ]
  edge [
    source 3
    target 4
    delay 15
    bw 0
  ]
]
