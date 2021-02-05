graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 8
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 16
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 55
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 195
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 111
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 132
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 155
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 132
  ]
]
