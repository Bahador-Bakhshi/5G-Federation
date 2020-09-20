graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 2
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 5
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 5
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 2
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 190
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 180
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 135
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 95
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 195
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 59
  ]
]
